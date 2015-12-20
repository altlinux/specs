Summary: A DBA's (s)wiss-(a)rmy-(k)nif(e) for mysql
Name: dbsake
License: GPLv2
Version: 2.1.0
Release: alt1
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

Packager: Evgenii Terechkov <evg@altlinux.org>

Group: Databases

BuildArch: noarch
Url: https://github.com/abg/dbsake

BuildRequires: python-module-setuptools python-module-sphinx

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

%build
%python_build
pushd docs
make html
popd

%install
%python_install
# remove pkg_resources dependency from setup.py console_scripts
cat <<EOF >| %buildroot%_bindir/%name
#!%{__python}
import sys

import dbsake.cli

if __name__ == '__main__':
    sys.exit(dbsake.cli.main())
EOF
chmod 0755 %buildroot%_bindir/%name

# Drop builtin bundler:
find %buildroot%python_sitelibdir/%name -type f -name '*distutils_ext.py*' -delete

%files
%_bindir/%name
%python_sitelibdir/%{name}*
%doc docs/_build/html HISTORY.rst README.rst AUTHORS.rst CONTRIBUTING.rst

%changelog
* Sun Dec 20 2015 Terechkov Evgenii <evg@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux Sisyphus
