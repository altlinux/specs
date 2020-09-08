%define        pkgname mixlib-shellout

Name: 	       gem-%pkgname
Version:       3.1.4
Release:       alt1
Summary:       mixin library for subprocess management, output collection
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-shellout
Vcs:           https://github.com/chef/mixlib-shellout.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Provides a simplified interface to shelling out yet still collecting
both standard out and standard error and providing full control over
environment, working directory, uid, gid, etc.

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

%files doc
%ruby_gemdocdir


%changelog
* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.4-alt1
- ^ 3.0.11 -> 3.1.4

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.11-alt1
- > Ruby Policy 2.0
- ^ 2.4.0 -> 3.0.11

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux
