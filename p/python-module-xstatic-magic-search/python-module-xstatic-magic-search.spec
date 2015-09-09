%global pypi_name xstatic-magic-search
%define version 0.2.0.1

%def_with python3

Name:           python-module-%pypi_name
Version:        %version
Release:        alt1
Group:          Development/Python
Summary:        Magic-Search (XStatic packaging standard)

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%pypi_name
Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires:  python-module-setuptools

%description
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Magic-Search (XStatic packaging standard)
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description -n python3-module-%pypi_name
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.
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
%python_sitelibdir/xstatic/pkg/magic_search
%python_sitelibdir/XStatic_Magic_Search-%version-py?.?.egg-info
%python_sitelibdir/XStatic_Magic_Search-%version-py?.?-nspkg.pth

%if_with python3
%files -n python3-module-%pypi_name
%doc README.txt
%python3_sitelibdir/xstatic/pkg/magic_search
%python3_sitelibdir/XStatic_Magic_Search-%version-py?.?.egg-info
%python3_sitelibdir/XStatic_Magic_Search-%version-py?.?-nspkg.pth
%endif

%changelog
* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 0.2.0.1-alt1
- First build for ALT (based on Fedora 0.2.0.1-2.fc23.src)
