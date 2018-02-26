%def_disable debug

%define cvsdate 20041220
%define bname intl
%define ename erlang-%bname
Name: %ename-drv
Version: 1.1
%define rel 3
Release: alt%{?cvsdate:0.}%rel
Summary: Internationalization localization driver for Erlang
License: %bsdstyle
Group: Development/Erlang
URL: http://jungerl.sourceforge.net
%ifdef cvsdate
#cvs -z3 -d:pserver:anonymous@jungerl.cvs.sourceforge.net:/cvsroot/jungerl co jungerl
Source: %bname-cvs-%cvsdate.tar
%else
Source: %bname-%version.tar
%endif
Patch0: %bname-makefile.patch
Patch1: %ename-alt.patch
Conflicts: jungerl < 0-alt0.20071220.1
Requires: erlang-otp-common
Packager: Sergey Shilov <hsv@altlinux.org>

BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: rpm-build-erlang rpm-build-licenses

%description
Internationalization localization driver for Erlang.


%package -n %ename
Summary: Internationalization localization for Erlang
Group: Development/Other
Requires: %name = %version
BuildArch: noarch

%description -n %ename
Internationalization localization for Erlang.


%prep
%setup -n %bname
%patch0 -p1
%patch1 -p1
mkdir -p ebin priv


%build
%define eoptflags -W +inline %{?_enable_debug:+debug_info}
%make_build ERLC_FLAGS="%{?eoptflags:%eoptflags}"


%install
for d in ebin include priv; do
    install -d -m 0755 %buildroot%_otplibdir/%bname-%version/$d
    install -m 0644 $d/* %buildroot%_otplibdir/%bname-%version/$d/
done


%files
%dir %_otplibdir/%bname-*
%_otplibdir/%bname-*/priv


%files -n %ename
%_otplibdir/%bname-*/ebin
%_otplibdir/%bname-*/include


%changelog
* Thu Aug 04 2011 Sergey Shilov <hsv@altlinux.org> 1.1-alt0.3
- rebuild with Erlang R14B03

* Sun Mar 20 2011 Sergey Shilov <hsv@altlinux.org> 1.1-alt0.2
- fix packager;
- fix BuildRequires: erlang -> erlang-otp-devel
- rebuild with Erlang R14B02

* Tue Aug 19 2008 Led <led@altlinux.ru> 1.1-alt0.1
- initial separate build
