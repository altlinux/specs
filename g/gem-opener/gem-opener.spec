%define        gemname opener

Name:          gem-opener
Version:       0.1.0
Release:       alt1.1
Summary:       A 33-line alternative to Ruby's launchy gem
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/sunaku/opener
Vcs:           https://github.com/sunaku/opener.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(opener) = 0.1.0


%description
Opener is a Ruby library for opening things in an cross-platform way.

It is a tiny (33 lines of code) alternative to the launchy library.


%package       -n gem-opener-doc
Version:       0.1.0
Release:       alt1.1
Summary:       A 33-line alternative to Ruby's launchy gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета opener
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(opener) = 0.1.0

%description   -n gem-opener-doc
A 33-line alternative to Ruby's launchy gem documentation files.

Opener is a Ruby library for opening things in an cross-platform way.

It is a tiny (33 lines of code) alternative to the launchy library.

%description   -n gem-opener-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета opener.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-opener-doc
%doc README.markdown
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1.1
- ! spec

* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
