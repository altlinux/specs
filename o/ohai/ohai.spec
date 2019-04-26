%define        pkgname ohai

Name:          %pkgname
Version:       15.0.34
Release:       alt1
Summary:       Ohai profiles your system and emits JSON
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chef/ohai
# VCS:         https://github.com/chef/ohai.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%filter_from_requires /wmi-lite/d

%description
Ohai is a tool that is used to detect attributes on a node, and then
provide these attributes to the chef-client at the start of every
chef-client run. Ohai is required by the chef-client and must be present
on a node.

%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%prep
%setup

%build
%gem_build --join=lib:bin

%install
%gem_install

%check
%gem_test

%files
%doc README*
%_bindir/%pkgname
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir

%changelog
* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 15.0.34-alt1
- New version.

* Mon Mar 25 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.30-alt1
- Bump to 15.0.30
- Use Ruby Policy 2.0

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.25-alt1
- New version.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.20-alt1
- New version.

* Wed Nov 21 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.7-alt1
- New version.

* Fri Oct 12 2018 Andrey Cherepanov <cas@altlinux.org> 14.6.2-alt1
- New version.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.9-alt1
- New version.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.7-alt1
- New version.

* Fri Sep 28 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.6-alt1
- New version.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.5-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.4-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.1-alt1
- New version.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Sat Jul 07 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.4-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.1-alt1
- New version.
- Package as gem.

* Thu Jun 14 2018 Dmitry Terekhin <jqt4@altlinux.org> 14.2.0-alt2
- Delete dependency "ruby-net-dhcp" for rebuild to mipsel.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.0-alt1
- New version.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.7-alt1
- New version.

* Tue May 22 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.6-alt1
- New version.

* Sun May 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.5-alt1
- New version.

* Sat May 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.4-alt1
- New version.

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.3-alt1
- New version.

* Tue May 15 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.2-alt1
- New version.

* Fri May 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.1-alt1
- New version.

* Sat May 05 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.0-alt1
- New version.

* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.34-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.32-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.31-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.30-alt1
- New version.

* Tue Mar 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.29-alt1
- New version.

* Sat Mar 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.28-alt1
- New version.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.26-alt1
- New version.

* Sat Mar 10 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.25-alt1
- New version.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.23-alt1
- New version.

* Wed Mar 07 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.22-alt1
- New version.

* Sat Mar 03 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.21-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.20-alt1
- New version.

* Tue Feb 27 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.15-alt1
- New version.

* Sat Feb 24 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.13-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.12-alt1
- New version.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.2-alt1
- New version.

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- New version.

* Thu Jan 11 2018 Andrey Cherepanov <cas@altlinux.org> 13.7.1-alt1
- New version.

* Wed Dec 06 2017 Andrey Cherepanov <cas@altlinux.org> 13.7.0-alt1
- New version.

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 13.6.0-alt1
- New version

* Fri Sep 29 2017 Andrey Cherepanov <cas@altlinux.org> 13.5.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.4.0-alt1
- New version

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 13.3.0-alt1
- New version

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 13.2.0-alt1
- New version

* Sat May 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Thu Apr 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.1-alt1
- New version

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 8.23.0-alt1
- new version 8.23.0

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 8.20.0-alt1
- new version 8.20.0

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt1
- New version

* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- Initial build for ALT Linux
