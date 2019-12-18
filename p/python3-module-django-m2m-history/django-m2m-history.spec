%define _unpackaged_files_terminate_build 1
%define oname django-m2m-history

Name: python3-module-%oname
Version: 0.3.6
Release: alt2

Summary: Django ManyToMany relation field with history of changes
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-m2m-history/
BuildArch: noarch

# https://github.com/ramusus/django-m2m-history.git
Source0: https://pypi.python.org/packages/27/46/9b3232433648020dff3d5def31446c095b86e20c7239ed2d4bcf29df689b/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Django ManyToMany relation field with history of changes. Like usual
Django's ManyToManyField, it's generate intermediary join table to
represent the many-to-many relationship, but with two additional
columns: 'time_from' and 'time_to'. Using updated interface of field
it's possible to retreive history of all versions of this field's value.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip fields models

%description tests
Django ManyToMany relation field with history of changes. Like usual
Django's ManyToManyField, it's generate intermediary join table to
represent the many-to-many relationship, but with two additional
columns: 'time_from' and 'time_to'. Using updated interface of field
it's possible to retreive history of all versions of this field's value.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.6-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20140425.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20140425
- Initial build for Sisyphus

