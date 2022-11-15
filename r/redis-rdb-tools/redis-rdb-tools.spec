%define pyname rdbtools

Name: redis-rdb-tools
Version: 0.1.15
Release: alt1.1

Summary: Parse Redis dump.rdb files, Analyze Memory, and Export Data to JSON

License: MIT License
Group: Databases
Url: https://rdbtools.com

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-url: https://github.com/sripathikrishnan/redis-rdb-tools/archive/rdbtools-%version.tar.gz
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
Requires: python3-module-%pyname = %EVR

Provides: rdbtools = %EVR


%description
Parse Redis dump.rdb files, Analyze Memory, and Export Data to JSON
Rdbtools is a parser for Redis' dump.rdb files.

The parser generates events similar to an xml sax parser,
and is very efficient memory wise.

In addition, rdbtools provides utilities to:
* Generate a Memory Report of your data across all databases and keys
* Convert dump files to JSON
* Compare two dump files using standard diff tools

%package -n python3-module-%pyname
Summary: Python3 module for %name
Group: Development/Python3

%description -n python3-module-%pyname
This package contains python3 module for %name.

%prep
%setup
#patch0 -p2

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name 'run_tests' \))

%package -n python3-module-%pyname-tests
Summary: Tests for %pyname
Group: Development/Python3
Requires: python3-module-%pyname = %EVR

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%pyname/tests/

%description -n python3-module-%pyname-tests
This package contains tests for %pyname.

%build
%python3_build

%install
%python3_install

cp -fR tests/ %buildroot%python3_sitelibdir/%pyname/

%files
%doc README.md docs/
%_bindir/rdb
%_bindir/redis-memory-for-key
%_bindir/redis-profiler

%files -n python3-module-%pyname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%pyname/tests/

%files -n python3-module-%pyname-tests
%python3_sitelibdir/%pyname/tests/


%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.1.15-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Jun 29 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1.15-alt1
- new version 0.1.15 (with rpmrb script)

* Fri Apr 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1.14-alt1
- new version 0.1.14 (with rpmrb script)

* Wed Jan 29 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.13-alt2
- Porting on Python3.

* Sat Dec 01 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1.13-alt1
- initial build for ALT Linux Sisyphus
