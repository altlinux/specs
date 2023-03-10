%define        _unpackaged_files_terminate_build 1
%define        gemname rack-jsonp

Name:          gem-rack-jsonp
Version:       1.3.2.1
Release:       alt0.1
Summary:       A Rack middleware for providing JSON-P support
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/crohr/rack-jsonp
Vcs:           https://github.com/crohr/rack-jsonp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0.8
BuildRequires: gem(rspec) >= 1.3
BuildRequires: gem(rack) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(rack) >= 0
Obsoletes:     ruby-rack-jsonp < %EVR
Provides:      ruby-rack-jsonp = %EVR
Provides:      gem(rack-jsonp) = 1.3.2.1

%ruby_use_gem_version rack-jsonp:1.3.2.1

%description
A Rack middleware for providing JSON-P support. Most of it is taken from the
original Rack::JSONP middleware present in rack-contrib.

Since I don't want to include the complete rack-contrib gem when all I need is
the JSONP middleware, I created this gem.


%package       -n gem-rack-jsonp-doc
Version:       1.3.2.1
Release:       alt0.1
Summary:       A Rack middleware for providing JSON-P support documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-jsonp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-jsonp) = 1.3.2.1

%description   -n gem-rack-jsonp-doc
A Rack middleware for providing JSON-P support documentation files.

A Rack middleware for providing JSON-P support. Most of it is taken from the
original Rack::JSONP middleware present in rack-contrib.

Since I don't want to include the complete rack-contrib gem when all I need is
the JSONP middleware, I created this gem.

%description   -n gem-rack-jsonp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-jsonp.


%package       -n gem-rack-jsonp-devel
Version:       1.3.2.1
Release:       alt0.1
Summary:       A Rack middleware for providing JSON-P support development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-jsonp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-jsonp) = 1.3.2.1
Requires:      gem(rake) >= 0.8
Requires:      gem(rspec) >= 1.3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-rack-jsonp-devel
A Rack middleware for providing JSON-P support development package.

A Rack middleware for providing JSON-P support. Most of it is taken from the
original Rack::JSONP middleware present in rack-contrib.

Since I don't want to include the complete rack-contrib gem when all I need is
the JSONP middleware, I created this gem.

%description   -n gem-rack-jsonp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-jsonp.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rack-jsonp-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-rack-jsonp-devel
%doc README.rdoc


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 1.3.2.1-alt0.1
- ^ 1.3.2 -> 1.3.2p1

* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1.2
- > Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1.1
- Rebuild for new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- New version.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus
