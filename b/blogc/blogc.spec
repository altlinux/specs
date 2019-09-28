Name: blogc
Version: 0.18.0
Release: alt1
License: BSD
Group: Text tools
Summary: A blog compiler
Url: https://github.com/blogc/blogc

# Repacked %url/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar

# Automatically added by buildreq on Sat Sep 28 2019
# optimized out: gem-mustache gem-power-assert gem-rdiscount gem-ronn glibc-kernheaders-generic glibc-kernheaders-x86 perl pkg-config python-base ruby ruby-bundler ruby-hpricot ruby-rake ruby-rdoc ruby-rubygems-update ruby-stdlibs sh4
BuildRequires: gem-did-you-mean git-core ronn ruby-minitest ruby-net-telnet ruby-test-unit ruby-xmlrpc

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
* Sat Sep 28 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.18.0-alt1
- Updated to 0.18.0.

* Fri Aug 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.17.0-alt1
- Updated to 0.17.0.

* Thu Mar 02 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12.0-alt1
- Initial build.
