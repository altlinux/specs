%define        gemname rtagstask

Name:          gem-rtagstask
Version:       0.0.4
Release:       alt1
Summary:       A Rake task for building vi and emacs tags
License:       Ruby
Group:         Development/Ruby
Url:           https://rubygems.org/gems/rtagstask
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rtags) > 0.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rtags) > 0.0.0
Provides:      gem(rtagstask) = 0.0.4

%description
A Rake task for building vi and emacs tags.


%package       -n gem-rtagstask-doc
Version:       0.0.4
Release:       alt1
Summary:       A Rake task for building vi and emacs tags documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rtagstask
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rtagstask) = 0.0.4

%description   -n gem-rtagstask-doc
A Rake task for building vi and emacs tags documentation files.

%description   -n gem-rtagstask-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rtagstask.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rtagstask-doc
%ruby_gemdocdir


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
