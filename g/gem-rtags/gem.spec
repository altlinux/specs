%define        gemname rtags

Name:          gem-rtags
Version:       0.97.1
Release:       alt1
Summary:       rtags is a Ruby replacement for ctags - allowing for name navigation in source code using vim, emacs and others
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/gaizka/rtags
Vcs:           https://github.com/gaizka/rtags.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rtags) = 0.97.1


%description
This is the original commit of the rtags source code as written by Keiju
ISHITSUKA as part of the irb project. Now irb has moved into the main Ruby
source tree rtags has become an independent project


%package       -n rtags
Version:       0.97.1
Release:       alt1
Summary:       rtags is a Ruby replacement for ctags - allowing for name navigation in source code using vim, emacs and others executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rtags
Group:         Other
BuildArch:     noarch

Requires:      gem(rtags) = 0.97.1

%description   -n rtags
rtags is a Ruby replacement for ctags - allowing for name navigation in source
code using vim, emacs and others executable(s).

This is the original commit of the rtags source code as written by Keiju
ISHITSUKA as part of the irb project. Now irb has moved into the main Ruby
source tree rtags has become an independent project

%description   -n rtags -l ru_RU.UTF-8
Исполнямка для самоцвета rtags.


%package       -n gem-rtags-doc
Version:       0.97.1
Release:       alt1
Summary:       rtags is a Ruby replacement for ctags - allowing for name navigation in source code using vim, emacs and others documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rtags
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rtags) = 0.97.1

%description   -n gem-rtags-doc
rtags is a Ruby replacement for ctags - allowing for name navigation in source
code using vim, emacs and others documentation files.

This is the original commit of the rtags source code as written by Keiju
ISHITSUKA as part of the irb project. Now irb has moved into the main Ruby
source tree rtags has become an independent project

%description   -n gem-rtags-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rtags.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n rtags
%doc README
%_bindir/rtags

%files         -n gem-rtags-doc
%doc README
%ruby_gemdocdir


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.97.1-alt1
- + packaged gem with Ruby Policy 2.0
