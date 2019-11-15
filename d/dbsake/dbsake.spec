Name: dbsake
Version: 2.1.0
Release: alt3

Summary: A DBA's (s)wiss-(a)rmy-(k)nif(e) for mysql
License: GPLv2
Group: Databases
Url: https://github.com/abg/dbsake
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python-tools-2to3


%description
dbsake (pronounced "dee-bee sah-kay") is a set of commands to assist with:

- Parsing MySQL .frm files and output DDL
- Splitting mysqldump output into a file per object
- Patching a my.cnf to remove or convert deprecated options
- Deploying a new standalone MySQL "sandbox" instance
- Decoding/encoding MySQL filenames
- Managing OS caching for a set of files

Read the documentation at: http://docs.dbsake.net

%prep
%setup
%patch0 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

pushd docs
make html
popd

%install
%python3_install

# remove pkg_resources dependency from setup.py console_scripts
cat <<EOF >| %buildroot%_bindir/%name
#!%{__python3}
import sys

import dbsake.cli

if __name__ == '__main__':
    sys.exit(dbsake.cli.main())
EOF
chmod 0755 %buildroot%_bindir/%name

# Drop builtin bundler:
find %buildroot%python3_sitelibdir/%name -type f -name '*distutils_ext.py*' -delete

%files
%_bindir/%name
%python3_sitelibdir/%{name}*
%doc docs/_build/html HISTORY.rst README.rst AUTHORS.rst CONTRIBUTING.rst


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.0-alt3
- python2 -> python3

* Mon Dec 21 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt2
- Add missed submodules

* Sun Dec 20 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux Sisyphus
