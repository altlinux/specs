# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname daemons

Name:          ruby-%pkgname
Version:       1.3.1
Release:       alt1
Summary:       A toolkit to create and control daemons in different ways
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/thuehlinger/daemons
%vcs           https://github.com/thuehlinger/daemons.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Daemons provides an easy way to wrap existing ruby scripts (for
example a self-written server) to be run as a daemon and to be
controlled by simple start/stop/restart commands.

You can also call blocks as daemons and control them from the
parent or just daemonize the current process.

Besides this basic functionality, daemons offers many advanced
features like exception backtracing and logging (in case your
ruby script crashes) and monitoring and automatic restarting of
your processes if they crash.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- Bump to 1.3.1
- Use Ruby Policy 2.0

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.1.0-alt1
- [1.1.0]

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.10-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 1.0.10-alt1
- Built for Sisyphus

