
Name:           python-module-virtkey
Version:        0.60.0
Release:        alt1.1.1

Summary:        Python extension for emulating keypresses and getting the keyboard geometry from the xserver
License:        LGPLv3+
Group:          Development/Python
URL:            https://launchpad.net/python-virtkey

Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        http://launchpad.net/python-virtkey/0.60/%version/+download/python-virtkey-%version.tar.gz

BuildPreReq:    python-devel python-module-setuptools rpm-build-python
BuildRequires:  libX11-devel libXtst-devel libgtk+2-devel

%description
python-virtkey is a python extension for emulating keypresses and
getting the keyboard geometry from the xserver.

%prep
%setup -q -n python-virtkey-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS docs/* NEWS README
%{python_sitelibdir}/virtkey.so
%{python_sitelibdir}/python_virtkey*.egg-info


%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.60.0-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.60.0-alt1.1
- Rebuild with Python-2.7

* Wed Oct 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.60.0-alt1
- Initial build in Sisyphus
