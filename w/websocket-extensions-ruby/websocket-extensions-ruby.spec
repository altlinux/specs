%define        pkgname       websocket-extensions-ruby
%define        gemname       websocket-extensions

Name:          %pkgname
Version:       0.1.4
Release:       alt1
Summary:       Generic extension management for WebSocket connections
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/faye/websocket-extensions-ruby
%vcs           https://github.com/faye/websocket-extensions-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A minimal framework that supports the implementation of WebSocket
extensions in a way that's decoupled from the main protocol. This
library aims to allow a WebSocket extension to be written and used with
any protocol library, by defining abstract representations of frames and
messages that allow modules to co-operate.


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
%ruby_build --use=%gemname --alias=%name --join=lib:bin

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
* Mon Aug 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
^ v0.1.4
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus
