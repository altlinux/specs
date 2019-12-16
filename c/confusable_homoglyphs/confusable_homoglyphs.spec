%define _unpackaged_files_terminate_build 1

Name: confusable_homoglyphs
Version: 3.0.0
Release: alt1

Summary: A homoglyph is two or more very similar graphemes, characters, or glyphs.
License: MIT
Group: Text tools
Url: https://pypi.python.org/pypi/confusable_homoglyphs/
BuildArch: noarch

# git clone https://github.com/vhf/confusable_homoglyphs
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

Requires: python3-module-%name = %EVR


%description
%summary

%package -n python3-module-%name
Summary: A python3 module for %name.
Group: Development/Python3

%description -n python3-module-%name
%summary

This package contains python3 module for %name.

%package -n python3-module-%name-tests
Summary: Tests for pytnon3-module-%name
Group: Development/Python3
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-tests
%summary

This package contains tests for pytnon3-module-%name.

%package -n python3-module-%name-pickles
Summary: Pickles for %name
Group: Development/Python3

%description -n python3-module-%name-pickles
%summary

This package contains pickles for %name.

%package -n python3-module-%name-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%name-docs
%summary

This package contains documentation for %name.

%prep
%setup

sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%name
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%name/

mv tests/ %buildroot/%python3_sitelibdir/%name/

%files
%doc LICENSE *.rst
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%name/tests
%exclude %python3_sitelibdir/*/pickle

%files -n python3-module-%name-pickles
%python3_sitelibdir/*/pickle

%files -n python3-module-%name-docs
%doc docs/_build/html/*

%files -n python3-module-%name-tests
%python3_sitelibdir/%name/tests


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus

