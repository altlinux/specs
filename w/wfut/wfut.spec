Name:           wfut
Version:        1.1.0
Release:        alt2_12
Summary:        Software updater tool for WorldForge applications

Group:          Development/C
License:        GPL+
URL:            http://www.worldforge.org
Source0:        http://downloads.sourceforge.net/worldforge/WFUT-1.1.0.tar.gz
Source1:        wfut.desktop
Source2:        wfut.png

BuildRequires:  gcc-java desktop-file-utils
Source44: import.info

%description
Software updater tool for WorldForge applications.


%prep
%setup -q -n WFUT-%{version}
sed -i -e 's/gcj -c/gcj $(RPM_OPT_FLAGS) -c/' src/Makefile.in


%build
# This should be compiling to native code now, making the JAR
# override unnecessary.  Leave it in for now as a reminder of
# how to use it with gcc's jar program.
JAR=fastjar
export JAR
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# The start script checks for a native binary, and if not found, will
# try to use java + jar file instead.  But we are only building the
# native binary, so don't bother with this check.
mv $RPM_BUILD_ROOT%{_bindir}/wfut-bin $RPM_BUILD_ROOT%{_bindir}/wfut

desktop-file-install                             \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
        %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_12
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_11
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_10
- rebuild with fixed sourcedep analyser (#27020)

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_10
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_9
- initial release by fcimport

