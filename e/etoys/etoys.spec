Name:           etoys
Version:        5.0.2408
Release:        alt1_2
Summary:        A media-rich model, game, and simulation construction kit and authoring tool

Group:          Games/Educational
License:        ASL 2.0 and MIT
URL:            http://squeakland.org/
BuildArch:      noarch

Source0:        http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.gz
Source2:        etoys.desktop
Source3:        etoys.png

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       squeak-vm >= 3.10
Requires:       shared-mime-info

# the macro find_lang assumes .mo files are in .../share/locale/...
#  but etoys puts them in .../share/etoys/locale/...
#  I don't know who's wrong
# Define localebug to work around this.

%define localebug 1
Source44: import.info

%description
Squeak Etoys was inspired by LOGO, PARC-Smalltalk, Hypercard, and starLOGO. It 
is a media-rich authoring environment with a simple powerful scripted object 
model for many kinds of objects created by end-users that runs on many 
platforms, and is free and open source. It includes 2D and 3D graphics, images, 
text, particles, pres-entations, web-pages, videos, sound and MIDI, etc. It 
includes the ability to share desktops with other Etoy users in real-time, so 
many forms of immersive mentoring and play can be done over the Internet.

%package       sugar
Summary:       Sugar activity wrapper for Etoys
Group:         Graphical desktop/Sugar
Requires:      sugar
Requires:      sugar-presence-service
Requires:      %{name} = %{version}-%{release}

%description   sugar
A Sugar activity that launches Etoys within the Sugar environment.

%prep
%setup -q

%build
./autogen.sh --prefix=%{_prefix}
make %{?_smp_mflags} V=1

%install
make install-etoys install-activity ROOT=%{buildroot}

# FIXME:
#  according to my reading of the sugar activity doc, this shouldn't
#  be necessary.  The bin/ directory of the activity should be added to 
#  the PATH.  But it doesn't seem to be for F-10.
cp %{buildroot}%{_datadir}/sugar/activities/Etoys.activity/bin/etoys-activity %{buildroot}%{_bindir}/

# these files will be put in std RPM doc location
rm -rf %{buildroot}%{_datadir}/doc/etoys

install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/etoys.png 

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%if 0 == 0%{?localebug}
%find_lang %{name}
%endif
mkdir -p %buildroot%_datadir/%name/fonts

%if 0 == 0%{?localebug}
%files -f %{name}.lang
%else
%files
%endif
%doc ChangeLog LICENSE NOTICE README
%dir %{_datadir}/etoys
%{_datadir}/etoys/
%{_bindir}/etoys
%{_bindir}/etoys-activity
%{_datadir}/mime/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%if 0%{?localebug}
%lang(bn) %{_datadir}/etoys/locale/bn
%lang(ru) %{_datadir}/etoys/locale/ru
%lang(de) %{_datadir}/etoys/locale/de
%lang(nl) %{_datadir}/etoys/locale/nl
%lang(ht) %{_datadir}/etoys/locale/ht
%lang(el) %{_datadir}/etoys/locale/el
%lang(ne) %{_datadir}/etoys/locale/ne
%lang(si) %{_datadir}/etoys/locale/si
%lang(te) %{_datadir}/etoys/locale/te
%lang(it) %{_datadir}/etoys/locale/it
%lang(ja) %{_datadir}/etoys/locale/ja
%lang(mr) %{_datadir}/etoys/locale/mr
%lang(ro) %{_datadir}/etoys/locale/ro
%lang(ur) %{_datadir}/etoys/locale/ur
%lang(mn) %{_datadir}/etoys/locale/mn
%lang(tr) %{_datadir}/etoys/locale/tr
%lang(es) %{_datadir}/etoys/locale/es
%lang(ar) %{_datadir}/etoys/locale/ar
%lang(pt) %{_datadir}/etoys/locale/pt_BR
%lang(fa) %{_datadir}/etoys/locale/fa_AF
%lang(fr) %{_datadir}/etoys/locale/fr
%lang(pt) %{_datadir}/etoys/locale/pt
%lang(ko) %{_datadir}/etoys/locale/ko
%lang(en) %{_datadir}/etoys/locale/en
%lang(bg) %{_datadir}/etoys/locale/bg
%lang(ps) %{_datadir}/etoys/locale/ps
%lang(sv) %{_datadir}/etoys/locale/sv
%lang(vi) %{_datadir}/etoys/locale/vi
%endif
%dir %_datadir/%name/fonts

%files sugar
%{_datadir}/sugar/activities/*

%changelog
* Thu Nov 29 2012 Igor Vlasenko <viy@altlinux.ru> 5.0.2408-alt1_2
- use F19 import base

* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.0.2048-alt1
- new version

* Tue Apr 06 2010 Aleksey Lim <alsroot@altlinux.org> 4.0.2340-alt1
- first build for ALT Linux Sisyphus

