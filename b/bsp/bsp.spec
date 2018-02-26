Name:           bsp
Version:        5.2
Release:        alt2_6
Summary:        The most popular node builder for Doom

Group:          Games/Other
License:        GPLv2+
URL:            http://games.moria.org.uk/doom/bsp/
Source0:        http://games.moria.org.uk/doom/bsp/download/%{name}-%{version}.tar.bz2
Source44: import.info

%description
Before you can play a level that you have created, you must use a node
builder to create the data that Doom will use to render the level.
Doom uses a rendering algorithm based on a binary space partition,
otherwise known as a BSP tree. This is stored in a data lump called
NODES in the WAD file. This data structure must be pre-calculated and
stored in the WAD file before the level can be played; the tool that
does this is called a node builder.

BSP is one of several node builders that can do this. There are
others: idbsp is the original node builder that id Software used on
the original Doom levels, for instance. BSP was the best known and
most widely used node builder throughout the height of the Doom
editing craze in the mid 1990s.


%prep
%setup -q
iconv -f ISO_8859-2 -t UTF8 bsp.6 > bsp.6.tmp
mv bsp.6.tmp bsp.6


%build
%configure
make CFLAGS='%{optflags}' %{?_smp_mflags}


%install
install -D -p -m 755 bsp $RPM_BUILD_ROOT/%{_bindir}/bsp
install -D -p -m 644 bsp.6 $RPM_BUILD_ROOT/%{_mandir}/man6/bsp.6


%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README visplane.txt test-wads/
%{_bindir}/bsp
%{_mandir}/man6/bsp.6*


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_6
- update to new release by fcimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_5
- converted from Fedora by srpmconvert script

