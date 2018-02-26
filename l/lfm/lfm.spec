Summary: powerful file manager for the console
Name: lfm
Version: 2.0
Release: alt1.1.1
Source0: %name-%version.tar.gz
Patch:	%name.alt.patch
License: GPL
Group: Development/Python
URL: https://inigo.katxi.org/devel/lfm/
Packager: Mikhail Pokidko <pma@altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Mon Mar 31 2008
BuildRequires: python-devel

%description
Last File Manager is a simple but powerful file manager for the UNIX console.

%prep
%setup  -q
%patch -p1

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES
sed -e "s/\.1/\.1.gz/" -i INSTALLED_FILES
#sed -e "s/\.1/\.1.gz/" -i INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.1
- Rebuilt with python 2.6

* Mon Mar 31 2008 Mikhail Pokidko <pma@altlinux.org> 2.0-alt1
- initial ALT build

