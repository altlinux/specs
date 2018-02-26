# TODO: there is exist driver registration utility, add some macros?
# odbcinst -i -d -f template

Name: mysql-connector-odbc
Version: 5.1.8
Release: alt1.1

Summary: MySQL Connector/ODBC - ODBC driver for MySQL

# exceptions allow library to be linked with most open source SW,
# not only GPL code.
License: GPLv2
Group: System/Libraries
Url: http://dev.mysql.com/doc/refman/5.0/en/myodbc-connector.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://mysql.mix.su/Downloads/Connector-ODBC/5.1/mysql-connector-odbc-%version.tar
Patch0: mysql-connector-odbc-5.1.8-alt-DSO.patch

# Automatically added by buildreq on Sat Jul 26 2008
BuildRequires: gcc-c++ glibc-devel libMySQL-devel libXt-devel libltdl-devel libunixODBC-devel unixODBC zlib-devel

BuildPreReq: libssl-devel

%description
MySQL Connector/ODBC (also known as MyODBC) allows you to connect
to a MySQL database server using the ODBC database API on all
Microsoft Windows and most Unix platforms, including through
such applications and programming environments such as
Microsoft Access, Microsoft Excel, and Borland Delphi.

Remember to check the Connector/ODBC documentation for detailed
installation and setup instructions at:
   http://dev.mysql.com/doc/refman/5.0/en/myodbc-connector.html

Connector/ODBC product information:
   http://www.mysql.com/products/myodbc/

Connector/ODBC mailing list archive:
   http://lists.mysql.com/myodbc

%prep
%setup
%patch0 -p2

%build
%configure --disable-gui
%make_build

%install
%makeinstall_std
# remove installed doc
rm -rf %buildroot%_datadir/%name/

%files
%doc ChangeLog README INSTALL LICENSE.gpl README.debug
%_bindir/myodbc-installer
%_libdir/lib*
#%_datadir/%name
#%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.8-alt1.1
- Fixed build

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.8-alt1
- 5.1.8

* Mon Oct 11 2010 Vitaly Lipatov <lav@altlinux.ru> 5.1.5-alt2
- fix build

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 5.1.5-alt1
- new version

* Sat Jul 26 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.4r1107-alt1
- new version 5.1.4

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 3.51-alt1
- rebuild with libMySQL 5.0
- add libssl-devel to build requires

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 3.51-alt0.1
- initial build for ALT Linux Sisyphus
- disable GUI
- build without MULTI_RESULTS support

