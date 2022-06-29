%define oname wsgicors

# See BAO #42228
%add_python3_req_skip nose
%def_disable check

Name:           python3-module-%oname
Version:        0.7.0
Release:        alt3

Summary:        WSGI for Cross Origin Resource Sharing (CORS)
Group:          Development/Python3
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/wsgicors
BuildArch:      noarch

# https://github.com/may-day/wsgicors.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
This is a WSGI middleware that answers CORS preflight requests and adds the needed header to the response.

For CORS see: http://www.w3.org/TR/cors/

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.rst LICENSE
%python3_sitelibdir/*

%changelog
* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt3
- Fixed BuildRequires.
- Build without check, because nose is deprecated.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt2
- python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
