%define module tokyocabinet
Name: ruby-%module
Version: 1.29
Release: alt2
Summary: Ruby binding to the Tokyo Cabinet
License: %lgpl2plus
Group: Development/Ruby
URL: http://%module.sourceforge.net
Source: %module-ruby-%version.tar
Provides: ruby-TokyoCabinet = %version-%release
Requires: libtokyocabinet >= 1.4.27
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses rpm-build-ruby
# Automatically added by buildreq on Thu Aug 14 2008
BuildRequires: bzlib-devel libruby-devel ruby ruby-module-etc
BuildRequires: zlib-devel
BuildRequires: libtokyocabinet-devel >= 1.4.27

%description
Ruby binding to the Tokyo Cabinet.


%package rdoc
Summary: rdoc documentation for Ruby binding to the Tokyo Cabinet
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release
Requires: ruby-tool-ri

%description rdoc
rdoc documentation for Ruby binding to the Tokyo Cabinet.


%package doc
Summary: Documentation for Ruby binding to the Tokyo Cabinet
Group: Documentation
BuildArch: noarch
Provides: %name-doc-html = %version-%release

%description doc
Documentation for Ruby binding to the Tokyo Cabinet.


%prep
%setup -n %module-ruby-%version


%build
%ruby_configure
%make_build


%install
%make_install DESTDIR=%buildroot install
install -d -m 0755 %buildroot%_docdir/%name-%version/{html,example}
install -m 0644 example/* %buildroot%_docdir/%name-%version/example/
cp -r doc/* %buildroot%_docdir/%name-%version/html/
%rdoc %module-doc.rb


%files
%ruby_sitearchdir/*.so


%files rdoc
%ruby_ri_sitedir/TokyoCabinet


%files doc
%_docdir/%name-%version
%exclude %_docdir/%name-%version/html/created.rid


%changelog
* Wed Nov 11 2009 Led <led@altlinux.ru> 1.29-alt2
- rebuild with libtokyocabinet.so.9

* Mon Jul 20 2009 Led <led@altlinux.ru> 1.29-alt1
- 1.29

* Thu Jul 16 2009 Led <led@altlinux.ru> 1.28-alt1
- 1.28

* Sat Jul 11 2009 Led <led@altlinux.ru> 1.27-alt1
- 1.27

* Sat Jun 27 2009 Led <led@altlinux.ru> 1.26-alt1
- 1.26

* Sun May 24 2009 Led <led@altlinux.ru> 1.25-alt1
- 1.25

* Sun Apr 26 2009 Led <led@altlinux.ru> 1.23-alt1
- 1.23

* Tue Apr 07 2009 Led <led@altlinux.ru> 1.22-alt1
- 1.22

* Wed Mar 11 2009 Led <led@altlinux.ru> 1.21-alt1
- 1.21

* Mon Feb 16 2009 Led <led@altlinux.ru> 1.20-alt1
- 1.20

* Sun Feb 15 2009 Led <led@altlinux.ru> 1.19-alt1
- 1.19

* Fri Jan 23 2009 Led <led@altlinux.ru> 1.18-alt2
- added exeptions

* Mon Dec 15 2008 Led <led@altlinux.ru> 1.18-alt1
- 1.18

* Sun Dec 07 2008 Led <led@altlinux.ru> 1.17-alt1
- 1.17

* Thu Oct 30 2008 Led <led@altlinux.ru> 1.16-alt1
- 1.16

* Tue Sep 09 2008 Led <led@altlinux.ru> 1.14-alt1
- 1.14

* Fri Aug 29 2008 Led <led@altlinux.ru> 1.13-alt1
- 1.13

* Fri Aug 15 2008 Led <led@altlinux.ru> 1.12-alt2
- added subpackage with rdoc documentation (thanx raorn@)

* Thu Aug 14 2008 Led <led@altlinux.ru> 1.12-alt1
- initial build
