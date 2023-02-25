Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           colordiff
Version:        1.0.21
Release:        alt1_3
Summary:        Color terminal highlighter for diff files

License:        GPL-2.0-or-later
URL:            http://www.colordiff.org/
Source0:        http://www.colordiff.org/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  rpm-build-perl
Requires:       diffutils
Requires:       less
Requires:     bzip2
Requires:     gzip gzip-utils
Requires:     xz
Requires:       curl
Provides:       cdiff
Source44: import.info

%description
Colordiff is a wrapper for diff and produces the same output but with
pretty syntax highlighting.  Color schemes can be customized.


%prep
%setup -q

# those are defaults of old 1.0.8a-alt1 by Pavlov Konstantin <thresh@>
sed -i -e 's/banner=yes/banner=no/' colordiffrc-*



%build


%install
%makeinstall_std INSTALL_DIR=%{_bindir} \
    ETC_DIR=%{_sysconfdir} MAN_DIR=%{_mandir}/man1


%files
%doc --no-dereference COPYING
%doc BUGS CHANGES colordiffrc colordiffrc-gitdiff colordiffrc-lightbg README
%config(noreplace) %{_sysconfdir}/colordiffrc
%{_bindir}/cdiff
%{_bindir}/colordiff
%{_mandir}/man1/cdiff.1*
%{_mandir}/man1/colordiff.1*


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.0.21-alt1_3
- update to new release by fcimport

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.0.21-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 1.0.20-alt1_1
- update to new release by fcimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.19-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.18-alt1_2
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.18-alt1_1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_3
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.16-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.15-alt1_1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_2
- update to new release by fcimport

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
