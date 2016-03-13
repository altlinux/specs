%global pypi_name xstatic-angular-lrdragndrop
%define version 1.0.2.2

%def_with python3

Name:           python-module-%pypi_name
Version:        %version
Release:        alt1.1
Group:          Development/Python
Summary:        Angular-lrdragndrop (XStatic packaging standard)

License:        MIT
URL:            http://pypi.python.org/pypi/%pypi_name
Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires:  python-module-setuptools

%description
lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Angular-lrdragndrop (XStatic packaging standard)
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description -n python3-module-%pypi_name
lrDragNDrop javascript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc README.txt
%{python_sitelibdir}/xstatic/pkg/angular_lrdragndrop
%{python_sitelibdir}/XStatic_Angular_lrdragndrop-%{version}-py?.?.egg-info
%{python_sitelibdir}/XStatic_Angular_lrdragndrop-%{version}-py?.?-nspkg.pth

%if_with python3
%files -n python3-module-%pypi_name
%doc README.txt
%{python3_sitelibdir}/xstatic/pkg/angular_lrdragndrop
%{python3_sitelibdir}/XStatic_Angular_lrdragndrop-%{version}-py?.?.egg-info
%{python3_sitelibdir}/XStatic_Angular_lrdragndrop-%{version}-py?.?-nspkg.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.2.2-alt1
- First build for ALT (based on Fedora 1.0.2.2-2.fc23.src)
