Name: rpcsvc-proto
Version: 1.4.2
Release: alt1

Summary: RPC protocol definitions
License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/thkukuk/rpcsvc-proto
Vcs: git://git.altlinux.org/gears/r/rpcsvc-proto.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
This package contains rpcsvc header files and RPC protocol definitions
from SunRPC sources (as used to be shipped with glibc).

%package devel
Summary: RPC protocol definitions
Group: Development/Other
BuildArch: noarch
Conflicts: glibc-devel < 6:2.32

%description devel
This package contains rpcsvc header files and RPC protocol definitions
from SunRPC sources (as used to be shipped with glibc).

%package -n rpcgen
Summary: RPC protocol compiler
Group: Development/Other
Conflicts: glibc-utils < 6:2.32

%description -n rpcgen
This package contains rpcgen - a tool that generates C code to implement
an RPC protocol.  The input to rpcgen is a language similar to C known
as RPC Language.

%prep
%setup
%autopatch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
# provided by quota-devel
rm %buildroot%_includedir/rpcsvc/rquota.[hx]

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%files devel
%_includedir/rpcsvc/

%files -n rpcgen
%_bindir/rpcgen
%_man1dir/rpcgen.1*
%doc COPYING

%changelog
* Sat Dec 19 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- Initial revision.
