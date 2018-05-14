
Name:           python-module-seamicroclient
Version:        0.1.0
Release:        alt2
Summary:        Python client for consuming SeaMicro REST API v2.0
Group:          Development/Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/python-seamicroclient/
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-pbr


%description
Python client for consuming SeaMicro REST API v2.0

%package -n python3-module-seamicroclient
Summary: Python client for consuming SeaMicro REST API v2.0
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-pbr

%description -n python3-module-seamicroclient
Python client for consuming SeaMicro REST API v2.0

%prep
%setup

# Remove bundled egg-info
rm -rf python_seamicroclient.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/*

%files -n python3-module-seamicroclient
%python3_sitelibdir/*


%changelog
* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 0.1.0-alt1
- First build for ALT

