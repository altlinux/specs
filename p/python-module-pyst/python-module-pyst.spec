%define module_name pyst

%def_without python3

Name: python-module-%module_name
Version: 0.6.50
Release: alt1

Summary: A Python Interface to Asterisk
License: PSF, LGPL
Group: Development/Python
Url: http://www.sourceforge.net/projects/pyst/

Source: python-module-%module_name-%version.tar

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
%endif

%setup_python_module %module_name

%description
%summary

%package -n python3-module-%module_name
Summary: A Python Interface to Asterisk
Group: Development/Python3

%description -n python3-module-%module_name
%summary

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc ChangeLog README*
%python_sitelibdir/asterisk
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%module_name
%doc ChangeLog README*
%python3_sitelibdir/asterisk
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.50-alt1
- Version 0.6.50

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.22-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.22-alt1
- Initial build for Sisyphus.
