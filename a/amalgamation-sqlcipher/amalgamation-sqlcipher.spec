Name: amalgamation-sqlcipher
Version: 2.1.0
Release: alt1.git20140824
Summary: %name for pysqlcipher
License: Free
Group: Development/Tools
Url: https://github.com/M0Rf30/amalgamation-sqlcipher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/M0Rf30/amalgamation-sqlcipher.git
Source: %name-%version.tar
BuildArch: noarch

%description
%name for pysqlcipher.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
install -p -m644 *.c *.h %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20140824
- Initial build for Sisyphus

