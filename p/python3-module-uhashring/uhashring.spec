%define  oname uhashring
%def_with check

Name:    python3-module-%oname
Version: 2.3
Release: alt1

Summary: Full featured consistent hashing python library compatible with ketama

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/uhashring

# https://github.com/ultrabug/uhashring
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-memcached
%endif

BuildArch: noarch

%description
uhashring implements consistent hashing in pure Python.

Consistent hashing is mostly used on distributed systems/caches/databases as this
avoid the total reshuffling of your key-node mappings when adding or removing a
node in your ring (called continuum on libketama). More information and details
about this can be found in the literature section.

This full featured implementation offers:
* a lot of convenient methods to use your consistent hash ring in real world
applications.
* simple integration with other libs such as memcache through monkey patching.
* a full ketama compatibility if you need to use it (see important mention below).
* all the missing functions in the libketama C python binding (which is not even
available on pypi) for ketama users.
* possibility to use your own weight and hash functions if you don't care about
the ketama compatibility.
* instance-oriented usage so you can use your consistent hash ring object
directly in your code (see advanced usage).
* native pypy support, since this is a pure python library.
* tests of implementation, key distribution and ketama compatibility.

Per node weight is also supported and will affect the nodes distribution on the
ring.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Mar 24 2023 Grigory Ustinov <grenka@altlinux.org> 2.3-alt1
- Automatically updated to 2.3.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 2.2-alt1
- Initial build for Sisyphus.
