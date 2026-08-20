%define _unpackaged_files_terminate_build 1
%def_with check

Name: nflxprofile
Version: 1.6.7
Release: alt1

Summary: Python package exposing the nflxprofile format as a Python class
License: MIT-Zero
Group: Development/Tools
Url: https://github.com/Netflix/nflxprofile
Vcs: https://github.com/Netflix/nflxprofile.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: protobuf-compiler
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-protobuf
%endif

Provides: python3-module-%name

%description
nflxprofile is a profiling/tracing format implemented using Protocol Buffers.
The goal of the format is to provide a compact yet complete and performant way
to store profiling and tracing events, which can later be used to generate
Flame Graphs, heat maps and other visualizations. It was first introduced in
FlameScope.

This package exposes the nflxprofile format as a Python class.

%prep
%setup
%autopatch -p1

%build
rm -vf python/nflxprofile/nflxprofile_pb2.py
%make python/nflxprofile/nflxprofile_pb2.py
cd python
%python3_build

%install
cd python
%python3_install
rm -rvf %buildroot%python3_sitelibdir_noarch/test

%check
cd python
%__python3 -m pytest

%files
%_bindir/%name
%python3_sitelibdir_noarch/%{name}*

%changelog
* Thu Aug 20 2026 Ivan A. Melnikov <iv@altlinux.org> 1.6.7-alt1
- build for Sisyphus
