Name: guile-json
Version: 3.3.0
Release: alt1

Summary: a JSON module for Guile
License: GPLv3+
Group: Development/Scheme

Source:%name-%version.tar

%ifarch %e2k
Buildrequires: guile20-devel libguile20-devel /proc
%else
BuildRequires: guile-devel >= 2.0
BuildRequires: /proc
%endif

%define _unpackaged_files_terminate_build 1

%description
guile-json is a JSON module for Guile. It supports parsing and
building JSON documents according to the http://json.org
specification.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%check
%make check

%install
%makeinstall_std

%define guile_sitedir %(guile-config info sitedir)

%files
%guile_sitedir/json.scm
%guile_sitedir/json
%guile_ccachedir/json.go
%guile_ccachedir/json.go
%guile_ccachedir/json

%changelog
* Wed Dec 25 2019 Paul Wolneykien <manowar@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
