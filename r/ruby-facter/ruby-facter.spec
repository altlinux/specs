%define        pkgname facter

Name: 	       ruby-%pkgname
Version:       2.5.2
Release:       alt1
Summary:       Ruby library for retrieving facts from operating systems
Group:         Development/Ruby
License:       Apache-2.0
Url:           https://tickets.puppetlabs.com/browse/FACT
%vcs           https://github.com/puppetlabs/facter
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcpp-hocon-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: libleatherman-devel
BuildRequires: boost-program_options-devel

Requires:      coreutils
Requires:      dmidecode
Requires:      net-tools
Requires:      pciutils
Requires:      bind-utils
%add_findreq_skiplist *.erb
%add_findreq_skiplist %ruby_gemslibdir/*

%description
A cross-platform Ruby library for retrieving facts from
operating systems. Supports multiple resolution mechanisms, any
of which can be restricted to working only on certain operating
systems or environments. Facter is especially useful for
retrieving things like operating system names, IP addresses, MAC
addresses, and SSH keys.

It is easy to extend Facter to include your own custom facts or
to include additional mechanisms for retrieving facts.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n facter
Summary:       Console executable called 'facter'
Group:         System/Base
BuildArch:     noarch

%description -n facter
%summary, for retrieving facts from
operating systems. Supports multiple resolution mechanisms, any
of which can be restricted to working only on certain operating
systems or environments. Facter is especially useful for
retrieving things like operating system names, IP addresses, MAC
addresses, and SSH keys.


%prep
%setup

%build
%ruby_build --ignore=acceptance

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%doc %_man8dir/%{pkgname}.*

%files         doc
%ruby_gemdocdir

%files         -n facter
%_bindir/*


%changelog
* Wed Jul 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- Bump to 2.5.2 with ALT support
- Fix spec

* Fri Feb 22 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt3
- Use Ruby Policy 2.0.

* Thu Dec 20 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt2
- Fixed ALT Release detection.
- Decrease timeout when accessing to EC2 from virtual env.
- Added facter executable rpm.
- Closes #35801.

* Tue Dec 18 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- Bump to 2.5.1.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2.1
- Rebuild with Ruby 2.4.1

* Wed Jan 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2
- Add ALT Linux operating system support
- Add bind-utils for IP address get

* Mon Apr 28 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version

* Fri Nov 30 2012 Led <led@altlinux.ru> 1.6.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Apr 27 2012 Sergey Alembekov <rt@altlinux.ru> 1.6.8-alt1
- [1.6.8]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.6-alt1
- [1.5.6]

* Fri Oct 31 2008 Sir Raorn <raorn@altlinux.ru> 1.5.2-alt1
- [1.5.2]

* Wed Sep 03 2008 Sir Raorn <raorn@altlinux.ru> 1.5.1-alt1
- Built for Sisyphus
