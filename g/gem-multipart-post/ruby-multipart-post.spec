%define        gemname multipart-post

Name:          gem-multipart-post
Version:       2.1.1
Release:       alt2
Summary:       Adds multipart POST capability to net/http
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nicksieger/multipart-post
Vcs:           https://github.com/nicksieger/multipart-post.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Obsoletes:     ruby-multipart-post < %EVR
Provides:      ruby-multipart-post = %EVR
Provides:      gem(multipart-post) = 2.1.1


%description
Adds a streamy multipart form post capability to Net::HTTP. Also supports other
methods besides POST.


%package       -n gem-multipart-post-doc
Version:       2.1.1
Release:       alt2
Summary:       Adds multipart POST capability to net/http documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета multipart-post
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(multipart-post) = 2.1.1

%description   -n gem-multipart-post-doc
Adds multipart POST capability to net/http documentation files.

Adds a streamy multipart form post capability to Net::HTTP. Also supports other
methods besides POST.

%description   -n gem-multipart-post-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета multipart-post.


%package       -n gem-multipart-post-devel
Version:       2.1.1
Release:       alt2
Summary:       Adds multipart POST capability to net/http development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета multipart-post
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(multipart-post) = 2.1.1
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4
Requires:      gem(rake) >= 0

%description   -n gem-multipart-post-devel
Adds multipart POST capability to net/http development package.

Adds a streamy multipart form post capability to Net::HTTP. Also supports other
methods besides POST.

%description   -n gem-multipart-post-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета multipart-post.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-multipart-post-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-multipart-post-devel
%doc README.md


%changelog
* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt2
- ! spec

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.0.0 -> 2.1.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 2.0.0-alt1
- Initial build in Sisyphus
