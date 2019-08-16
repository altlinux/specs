%define _unpackaged_files_terminate_build 1
%define pypi_name livereload

%def_with check

Name: python-module-%pypi_name
Version: 2.6.1
Release: alt1
Summary: Utility for starting a server in a directory
License: BSD
Url: https://github.com/lepture/python-livereload
Group: Development/Python
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python2.7(nose)
BuildRequires: python2.7(tornado)
BuildRequires: python3(nose)
BuildRequires: python3(tornado)
%endif

# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python2\.7(django\(\..*\)\?)/d
%filter_from_requires /^python3(django\(\..*\)\?)/d

%description
LiveReload provides a command line utility, livereload, for starting
a server in a directory. By default, it will listen to port 35729,
the common port for LiveReload browser extensions. LiveReload is designed
for web developers who know Python.

%package -n python3-module-%pypi_name

Summary: Command line utility for starting a server in a directory
Group: Development/Documentation

%description -n python3-module-%pypi_name
Python3 LiveReload provides a command line utility, livereload, for
starting a server in a directory. By default, it will listen to port
35729, the common port for LiveReload browser extensions. LiveReload
is designed for web developers who know Python.

%prep
%setup
%patch -p1

cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
nosetests -s
pushd ../python3
nosetests3 -s
popd

%files -n python3-module-%pypi_name
%doc README.rst CHANGES.rst LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version-py?.?.egg-info

%files -n python-module-%pypi_name
%doc README.rst CHANGES.rst LICENSE
%python_sitelibdir/%pypi_name
%python_sitelibdir/%pypi_name-%version-py?.?.egg-info

%changelog
* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 2.6.1-alt1
- 2.5.1 -> 2.6.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.1-alt2
- Fixed build.

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 2.5.1-alt1
- Initial build for ALT (based on 2.5.1-2.fc26.src)

