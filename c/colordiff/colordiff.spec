# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/python-config binutils-devel cmake elfutils-devel gcc-c++ libelf-devel perl(IPC/Open2.pm) python-devel
# END SourceDeps(oneline)
Group: Text tools
Name:           colordiff
Version:        1.0.13
Release:        alt1_1
Summary:        Color terminal highlighter for diff files

License:        GPLv2+
URL:            http://www.colordiff.org/
Source0:        http://www.colordiff.org/%{name}-%{version}.tar.gz
# Non-upstream, better default colors for Fedora default desktop themes
Patch0:         %{name}-1.0.6-colors.patch

BuildArch:      noarch
Requires:       xz
Requires:       bzip2
Requires:       gzip
Requires:       less
Requires:       diffutils
Requires:       which
Provides:       cdiff
Source44: import.info

%description
Colordiff is a wrapper for diff and produces the same output but with
pretty syntax highlighting.  Color schemes can be customized.


%prep
%setup -q
%patch0 -p1
mv colordiffrc colordiffrc-darkbg ; cp -p colordiffrc-lightbg colordiffrc

# those are defaults of old 1.0.8a-alt1 by Pavlov Konstantin <thresh@>
sed -i -e 's/banner=yes/banner=no/' colordiffrc-*



%build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_DIR=%{_bindir} \
    ETC_DIR=%{_sysconfdir} MAN_DIR=%{_mandir}/man1


%files
%doc BUGS CHANGES colordiffrc-darkbg colordiffrc-lightbg COPYING README
%config(noreplace) %{_sysconfdir}/colordiffrc
%{_bindir}/cdiff
%{_bindir}/colordiff
%{_mandir}/man1/cdiff.1*
%{_mandir}/man1/colordiff.1*


%changelog
* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_1
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.12-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_5
- update to new release by fcimport

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_4
- new version by fcimport

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.8a-alt1
- 1.0.8a release.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.7-alt1
- 1.0.7 release.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.6a-alt1
- 1.0.6a release.

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.0.6-alt1
- 1.0.6 release.

* Mon Nov 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5-alt2
- Changed default output to more common colors.

* Mon Nov 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5-alt1
- Initial build for Sisyphus.
- Cleaned up fedora core spec file.

* Wed Aug 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.5-2
- Drop no longer needed Obsoletes.

* Sat May 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.5-1
- Add version to cdiff Obsoletes (Matthias Saou).
- Require diffutils (Matthias Saou, Matthew Miller).

* Mon Mar 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.5-0.1
- 1.0.5.

* Thu Mar 17 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.0.4-0.1
- Disable banner display in default configs.
- Drop unnecessary Epochs.

* Fri Aug 13 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0.4-0.fdr.3
- Apply upstream fix for context diff detection.

* Thu Aug 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0.4-0.fdr.2
- Use lightbg as the default scheme and make it work better with dark
  backgrounds too.

* Sat Jul 17 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0.4-0.fdr.1
- First build.
- Include cdiff wrapper.
