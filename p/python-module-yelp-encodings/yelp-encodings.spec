%define oname yelp-encodings

%def_with python3

Name:           python-module-%oname
Version:        0.1.3
Release:        alt1
Summary:        String encodings invented and maintained by yelp.
Group:          Development/Python
License:        Unlicense
URL:            https://pypi.python.org/pypi/yelp_encodings
BuildArch:      noarch

# https://github.com/Yelp/yelp_encodings.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%endif

%description
yelp_encodings contains an 'internet' encoding which is appropriate
for dealing with poorly encoded bytes coming from internet clients.
The internet encoding will always succeed in decoding any bytestring.
This is most often useful for logging bad requests.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        String encodings invented and maintained by yelp.

%description -n python3-module-%oname
yelp_encodings contains an 'internet' encoding which is appropriate
for dealing with poorly encoded bytes coming from internet clients.
The internet encoding will always succeed in decoding any bytestring.
This is most often useful for logging bad requests.
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
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
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
* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt1
- Initial build for ALT.
