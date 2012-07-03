%define _unpackaged_files_terminate_build 1
%def_disable debug

%define bname rfc4627

Name: erlang-%bname
Version: 1.1.1
Release: alt1.hg.98
License: MPLv1.1
Group: Development/Erlang
Source: %name-%version.tar
URL: http://hg.opensource.lshift.net/erlang-rfc4627/
Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-macros-erlang
BuildRequires: erlang-devel erlang-otp-devel zip
Requires: erlang
Summary: Erlang RFC4627 (JSON) codec and JSON-RPC server implementation

%description
A JSON (RFC4627) codec and JSON-RPC server for Erlang

%package -n %name-devel
Summary: %name header files
License: MPLv1.1
Group: Development/Erlang

%description -n %name-devel
Erlang header files for %name 

%prep
%setup -q

%build
%define eoptflags -W +inline %{?_enable_debug:+debug_info}
%make_build ERLC_FLAGS="%{?eoptflags:%eoptflags}"
%make doc

%install
mkdir -p %buildroot%_erlanglibdir/%bname-%version
cp -r ebin %buildroot%_erlanglibdir/%bname-%version

mkdir -p %buildroot%_erlanglibdir/%bname-%version/
cp -r include %buildroot%_erlanglibdir/%bname-%version/

mkdir -p %buildroot%_docdir/%bname-%version
cp -r doc %buildroot%_docdir/%bname-%version

%files
%_erlanglibdir/%bname-%version/ebin

%files -n %name-devel
%_erlanglibdir/%bname-%version/include
%doc %_docdir/*

%changelog
* Thu Sep 17 2009 Maxim Ivanov <redbaron at altlinux.org> 1.1.1-alt1.hg.98
- Bump to changeset 98
- Correct version in spec

* Tue Jul 21 2009 Maxim Ivanov <redbaron at altlinux.org> 0.01-alt1
- Initial build for ALTLinux

