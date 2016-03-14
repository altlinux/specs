%def_with python3

%global pypi_name lesscpy

Name:           python-module-%{pypi_name}
Version:        0.10.1
Release:        alt1.1.1
Summary:        Lesscss compiler
Group:          Development/Python

License:        MIT
URL:            https://github.com/robotis/lesscpy
Source0:        %{name}-%{version}.tar
BuildArch:      noarch
 
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-mccabe python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-tools-pep8 python3 python3-base python3-module-mccabe python3-module-setuptools python3-pyflakes python3-tools-pep8
BuildRequires: python-module-coverage python-module-flake8 python-module-nose python3-module-coverage python3-module-flake8 python3-module-nose rpm-build-python3

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-ply
#BuildRequires:  python-module-nose
#BuildRequires:  python-module-coverage
#BuildRequires:  python-module-flake8
 
Requires:       python-module-ply
%description
A compiler written in python 3 for the lesscss language.  For those of us not 
willing/able to have node.js installed in our environment.  Not all features 
of lesscss are supported (yet).  Some features wil probably never be 
supported (JavaScript evaluation). 

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:    Lesscss compiler
Group:      Development/Python
Requires:   python3-module-ply
#BuildRequires: rpm-build-python3
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-ply
#BuildRequires: python3-module-nose
#BuildRequires: python3-module-flake8
#BuildRequires: python3-module-coverage
%description -n python3-module-%{pypi_name}
A compiler written in python 3 for the lesscss language.  For those of us not
willing/able to have node.js installed in our environment.  Not all features
of lesscss are supported (yet).  Some features wil probably never be
supported (JavaScript evaluation).
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
#fix utf8 encoding issue occurring only under py3
pushd ../python3
find ../python3 -name '*.py' | xargs sed -i '1s|^#!/usr/bin/python|#!%{__python3}|'
popd
%endif

%build
%python_build
%if_with python3
pushd ../python3
export LANG=en_US.utf8
env
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
mv %{buildroot}/%{_bindir}/lesscpy %{buildroot}/%{_bindir}/py3-lesscpy
popd
%endif

%python_install

#%check
#nosetests -v 
#%if_with python3
#pushd %%{py3dir}
#nosetests-3.3 -v
#popd
#%endif

%files
%doc LICENSE
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%{_bindir}/lesscpy
%if_with python3
%files -n python3-module-%{pypi_name}
%doc LICENSE
%{_bindir}/py3-lesscpy
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}*.egg-info
%endif


%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.10.1-alt1
- First build for ALT (based on Fedora 0.10.1-3.fc21.src)

