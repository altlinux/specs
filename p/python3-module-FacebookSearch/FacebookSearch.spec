%define _unpackaged_files_terminate_build 1
%define oname FacebookSearch

Name: python3-module-%oname
Version: 0.0.3
Release: alt3

Summary: A Python library to easily iterate public information found by the Facebook Graph API
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/FacebookSearch/
# https://github.com/ckoepp/FacebookSearch.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
This library is in a very early stage of development and due to this
there no documentation available (besides the source itself :p).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt3
- python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt2.git20131203.qa1
- NMU: applied repocop patch

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.3-alt2.git20131203
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20131203.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20131203
- Initial build for Sisyphus

