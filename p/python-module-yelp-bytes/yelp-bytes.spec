%define oname yelp-bytes

%def_with python3

Name:           python-module-%oname
Version:        0.3.0
Release:        alt2.qa1
Summary:        Utilities for dealing with byte strings, invented and maintained by Yelp.
Group:          Development/Python
License:        Unlicense
URL:            https://pypi.python.org/pypi/yelp_bytes
BuildArch:      noarch

# https://github.com/Yelp/yelp_bytes.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(yelp_encodings)
BuildRequires: python2.7(pytest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(yelp_encodings)
BuildRequires: python3(pytest)
%endif

%description
yelp_bytes contains several utility functions to help ensure
that the data you're using is always either Unicode or byte strings,
taking care of the edge cases for you so that you don't have to worry about them.
We handle ambiguous bytestrings by leveraging our our "internet" encoding.
This allows you to write functions that need unicode but can accept arbitrary values without crashing.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        Utilities for dealing with byte strings, invented and maintained by Yelp.

%description -n python3-module-%oname
yelp_bytes contains several utility functions to help ensure
that the data you're using is always either Unicode or byte strings,
taking care of the edge cases for you so that you don't have to worry about them.
We handle ambiguous bytestrings by leveraging our our "internet" encoding.
This allows you to write functions that need unicode but can accept arbitrary values without crashing.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
py.test

%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%doc README.md UNLICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md UNLICENSE
%python3_sitelibdir/*
%endif

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2.qa1
- NMU: applied repocop patch

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt2
- Updated build dependencies.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1
- Initial build for ALT.
