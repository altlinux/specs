%def_with debug
%def_with native
#----------------------------------------------------------------------
%define set_without() %{expand:%%force_without %{1}} %{expand:%%undefine _with_%{1}}

%define cvsdate 20071220
%define bname pgsql
%define pname erlang-%bname
Name: %bname-erl
Version: 0.0
%define rel 3
Release: alt%{?cvsdate:0.}%rel
Summary: PostgreSQL frontend for Erlang
License: EPL
Group: Development/Erlang
URL: http://jungerl.sourceforge.net
%ifdef cvsdate
#cvs -z3 -d:pserver:anonymous@jungerl.cvs.sourceforge.net:/cvsroot/jungerl co jungerl
Source: %bname-cvs-%cvsdate.tar
%else
Source: %bname-%version.tar
%endif
Patch0: %bname-alt.patch
Patch1: %bname-makefile.patch
#BuildArch: noarch
Conflicts: jungerl < 0-alt0.20071220.1
Requires: erlang-otp-common

BuildRequires: erlang rpm-build-erlang symlinks
%{?_with_native:BuildRequires: /proc}

%description
Second attempt at writing a PostgreSQL frontend. Connects by plain tcp
and should be able to perform simple SQL commands.


%package -n %pname
Summary: PostgreSQL frontend for Erlang
Group: Development/Erlang
BuildArch: noarch

%description -n %pname
Second attempt at writing a PostgreSQL frontend. Connects by plain tcp
and should be able to perform simple SQL commands.


%if_with debug
%package -n %pname-debug
Summary: PostgreSQL frontend for Erlang - modules with debug information
Group: Development/Erlang
BuildArch: noarch
Requires: %pname = %version-%release

%description -n %pname-debug
Second attempt at writing a PostgreSQL frontend. Connects by plain tcp
and should be able to perform simple SQL commands.
This package contains modules with debug information.
%endif


%if_with native
%package -n %pname-native
Summary: PostgreSQL frontend for Erlang - modules with native CPU code
Group: Development/Erlang
Requires: %pname = %version-%release

%description -n %pname-native
Second attempt at writing a PostgreSQL frontend. Connects by plain tcp
and should be able to perform simple SQL commands.
This package contains modules with native CPU code.
%endif


%prep
%setup -n %bname
%patch0 -p1
%patch1 -p1


%build
# Can't build HIPE'd modules on %ix86 :(
%ifnarch x86_64 k8 opteron
%set_without native
%endif
%make_build ERLC_FLAGS="%{?eoptflags:%eoptflags}"
%{?_with_debug:%make_build ERLC_FLAGS="%{?eoptflags:%eoptflags} +debug_info" EBIN_DIR=../ebin.debug}
%{?_with_native:%make_build ERLC_FLAGS="%{?eoptflags:%eoptflags} +native +'{hipe,[o2]}'" EBIN_DIR=../ebin.native}


%install
install -d %buildroot{%_otplibdir/%bname-%version/{doc,ebin},%_docdir/%pname-%version}
install -m 0644 ebin/* %buildroot%_otplibdir/%bname-%version/ebin/
install -m 0644 doc/* %buildroot%_otplibdir/%bname-%version/doc/
ln -sf %buildroot{%_otplibdir/%bname-%version/doc,%_docdir/%pname-%version}
%if_with debug
install -d %buildroot%_otplibdir/%bname-%version/ebin.debug
install -m 0644 ebin.debug/* %buildroot%_otplibdir/%bname-%version/ebin.debug/
%endif
%if_with native
install -d %buildroot%_otplibdir/%bname-%version/ebin.native
install -m 0644 ebin.native/* %buildroot%_otplibdir/%bname-%version/ebin.native/
%endif
symlinks -csd %buildroot%_docdir/%pname-%version


%files -n %pname
%dir %_otplibdir/%bname-%version
%_otplibdir/%bname-%version/doc
%_otplibdir/%bname-%version/ebin
%_docdir/*


%if_with debug
%files -n %pname-debug
%_otplibdir/%bname-%version/ebin.debug
%endif


%if_with native
%files -n %pname-native
%_otplibdir/%bname-%version/ebin.native
%endif


%changelog
* Wed Sep 10 2008 Led <led@altlinux.ru> 0.0-alt0.3
- fixed spec

* Tue Sep 09 2008 Led <led@altlinux.ru> 0.0-alt0.2
- updated %bname-makefile.patch
- added -native and -debug subpackages

* Sun Jul 27 2008 Led <led@altlinux.ru> 0.0-alt0.1
- initial separate build
