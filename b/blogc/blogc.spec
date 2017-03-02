Name: blogc
Version: 0.12.0
Release: alt1
License: BSD
Group: Text tools
Summary: A blog compiler
Url: https://github.com/blogc/blogc

# Repacked %url/archive/%version/%name-%version.tar.gz
Source0: blogc-0.12.0.tar

# Automatically added by buildreq on Thu Mar 02 2017
# optimized out: perl pkg-config python-base
BuildRequires: git-core

%{?!_without_check:%{?!_disable_check:BuildPreReq: libcmocka-devel}}

%description
blogc(1) is a blog compiler. It converts source files and templates into
blog/website resources.

%package git-receiver
Summary: A simple login shell/git hook to deploy blogc websites
Group: Text tools
Requires: git, tar, make

%description git-receiver
blogc-git-receiver is a simple login shell/git hook to deploy blogc websites.

%package runserver
Summary: A simple HTTP server to test blogc websites
Group: System/Servers

%description runserver
blogc-runserver is a simple HTTP server to test blogc websites.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-git-receiver \
	--enable-runserver \
	--enable-tests \
	#
%make_build

%check
make check

%install
%makeinstall_std

%files
%_man1dir/blogc.*
%_man7dir/blogc-source.*
%_man7dir/blogc-template.*
%_man7dir/blogc-pagination.*
%_bindir/blogc
%doc README.md

%files git-receiver
%_man1dir/blogc-git-receiver.*
%_bindir/blogc-git-receiver

%files runserver
%_man1dir/blogc-runserver.*
%_bindir/blogc-runserver

%changelog
* Thu Mar 02 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12.0-alt1
- Initial build.
