%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	PEAR_PackageFileManager2
Summary:	PEAR Package FileManager
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	45e5800e2ce249bad4fb4ef32da0de9d
URL:		http://pear.php.net/package/PEAR_PackageFileManager2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.8.0-0.alpha1
Requires:	php-pear-PEAR_PackageFileManager_Plugins
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(PHP/CompatInfo.*)

%description
This package revolutionizes the maintenance of PEAR packages. With a
few parameters, the entire package.xml is automatically updated with a
listing of all files in a package. Features include
 - manages the new package.xml 2.0 format in PEAR 1.4.0
 - can detect PHP and extension dependencies using PHP_CompatInfo
 - reads in an existing package.xml file, and only changes the
   release/changelog
 - a plugin system for retrieving files in a directory. Currently four
   plugins exist, one for standard recursive directory content listing,
   one that reads the CVS/Entries files and generates a file listing
   based on the contents of a checked out CVS repository, one that reads
   Subversion entries files, and one that queries a Perforce repository.
 - incredibly flexible options for assigning install roles to
   files/directories
 - ability to ignore any file based on a * ? wildcard-enabled string(s)
 - ability to include only files that match a * ? wildcard-enabled
   string(s)
 - ability to manage dependencies
 - can output the package.xml in any directory, and read in the
   package.xml file from any directory.
 - can specify a different name for the package.xml file

In PEAR status of this package is: %{_status}.

%prep
%pear_package_setup

mv docs/PEAR_PackageFileManager2/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PEAR/PackageFileManager2.php

%{_examplesdir}/%{name}-%{version}
