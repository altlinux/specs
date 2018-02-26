%def_disable debug

%define cvsdate 20070824
%define bname gettext
Name: erlang-%bname
Version: 1.3.0
%define rel 3
Release: alt%{?cvsdate:0.}%rel
Summary: gettext handling for Erlang
License: %bsdstyle
Group: Development/Erlang
URL: http://jungerl.sourceforge.net
%ifdef cvsdate
#cvs -z3 -d:pserver:anonymous@jungerl.cvs.sourceforge.net:/cvsroot/jungerl co jungerl
Source: %bname-cvs-%cvsdate.tar
%else
Source: %bname-%version.tar
%endif
Patch: %bname-makefile.patch
BuildArch: noarch
Conflicts: jungerl < 0-alt0.20071220.1
Requires: erlang-otp
Packager: Sergey Shilov <hsv@altlinux.org>

# Automatically added by buildreq on Tue Aug 19 2008
BuildRequires: erlang-devel erlang-otp-devel
BuildRequires: rpm-build-erlang rpm-build-licenses

%description
The '%bname' application makes it possible to internationalize your
application.
The name '%bname' comes from the GNU package with the same name.
However, the only thing they have in common is the format of the
PO-files, i.e the files containing the text that can be translated.


%prep
%setup -n %bname
%patch -p1
mkdir -p ebin


%build
%define eoptflags -W +inline %{?_enable_debug:+debug_info}
%make_build ERLC_FLAGS="%{?eoptflags:%eoptflags}"


%install
for d in ebin include; do
    install -d -m 0755 %buildroot%_otplibdir/%bname-%version/$d
    install -m 0644 $d/* %buildroot%_otplibdir/%bname-%version/$d/
done


%files
%doc LICENSE README
%_otplibdir/*


%changelog
* Thu Aug 04 2011 Sergey Shilov <hsv@altlinux.org> 1.3.0-alt0.3
- rebuild with Erlang R14B03

* Sun Mar 20 2011 Sergey Shilov <hsv@altlinux.org> 1.3.0-alt0.2
- fix packager;
- fix BuildRequires: erlang -> erlang-otp-devel
- rebuild with Erlang R14B02

* Tue Aug 19 2008 Led <led@altlinux.ru> 1.3.0-alt0.1
- initial separate build
