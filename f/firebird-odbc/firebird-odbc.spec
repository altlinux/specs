%define oname OdbcJdbc
Name: firebird-odbc
Version: 2.0.0147
Release: alt2

Summary: Firebird ODBC/JDBC Drivers

License: IDPLicense
Url: http://www.firebirdsql.org/
Group: Databases
Packager: Boris Savelev <boris@altlinux.org>
Source: %oname.tar.bz2

# Automatically added by buildreq on Wed Aug 20 2008
BuildRequires: firebird-devel gcc-c++ libunixODBC-devel

%description
The driver has undergone many improvements since the original release.
This document attempts to highlight the main changes. It is not intended
that this document provides a detailed technical explanation of them.

%package docs
Summary: Html docs for Firebird ODBC/JDBC Drivers
Group: Books/Other
BuildArch: noarch

%description docs
Html docs for Firebird ODBC/JDBC Drivers

%prep
%setup -q -n %oname

%build
pushd Builds/Gcc.lin
%make_build -f makefile.linux
popd

%install
find %_builddir/ -type d -name CVS | xargs rm -rf
%set_verify_elf_method textrel=relaxed
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_datadir/%name
cp Install/Linux/*.ini %buildroot%_datadir/%name/
cp Builds/Gcc.lin/Release/*.so %buildroot%_libdir

%files
%doc ChangeLog *.log Install/IDPLicense.txt Install/ReleaseNotes_v1.2.html
%_libdir/lib*
%dir %_datadir/%name/
%_datadir/%name/*.ini

%files docs
%doc Install/HtmlHelp*

%changelog
* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0147-alt2
- fix build

* Tue Oct 07 2008 Boris Savelev <boris@altlinux.org> 2.0.0147-alt1
- new version
- fix x86_64 build

* Wed Aug 20 2008 Boris Savelev <boris@altlinux.org> 2.0.0144-alt1
- initial build

