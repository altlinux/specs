%define _unpackaged_files_terminate_build 1

%define modname django_comments
%define oname django-contrib-comments

Name: python3-module-%oname
Version: 1.9.2
Release: alt1.1

Summary: Django "excontrib" Comments
License: BSD
Group: Development/Python3
Url: https://github.com/django/django-contrib-comments
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%modname/tests

%description
This framework can be used to attach comments to any model, so you can use it
for comments on blog entries, photos, book chapters, or anything else.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This framework can be used to attach comments to any model, so you can use it
for comments on blog entries, photos, book chapters, or anything else.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

mv tests/ %buildroot%python3_sitelibdir/%modname/

%files
%doc *.rst *.txt docs/
%python3_sitelibdir/%modname
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%modname/tests

%files tests
%python3_sitelibdir/%modname/tests


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.9.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.2-alt1
- Initial build for Sisyphus

