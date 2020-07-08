%define        pkgname mixlib-log

Name: 	       gem-%pkgname
Version:       3.0.8
Release:       alt1
Summary:       A simple class based Log mechanism, similar to Merb and Chef, that you can mix in to your project
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-log
#Vcs:           https://github.com/chef/mixlib-log.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Mixlib::Log provides a mixin for enabling a class based logger object,
a-la Merb, Chef, and Nanite.


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
* Fri Jul 10 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.8-alt1
- > Ruby Policy 2.0
- ^ 2.0.7 -> 3.0.8
- ! spec tags

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1
- New version.

* Fri Aug 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version.
- Package as gem.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- New version.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Initial build for ALT Linux
