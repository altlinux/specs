%define        gemname permessage_deflate

Name:          gem-permessage-deflate
Version:       0.1.4
Release:       alt1
Summary:       Per-message DEFLATE compression extension for WebSocket connections
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/faye/permessage-deflate-ruby
Vcs:           https://github.com/faye/permessage-deflate-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(permessage_deflate) = 0.1.4

%description
Implements the permessage-deflate WebSocket protocol extension as a plugin for
websocket-extensions.


%package       -n gem-permessage-deflate-doc
Version:       0.1.4
Release:       alt1
Summary:       Per-message DEFLATE compression extension for WebSocket connections documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета permessage_deflate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(permessage_deflate) = 0.1.4

%description   -n gem-permessage-deflate-doc
Per-message DEFLATE compression extension for WebSocket connections
documentation files.

Implements the permessage-deflate WebSocket protocol extension as a plugin for
websocket-extensions.

%description   -n gem-permessage-deflate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета permessage_deflate.


%package       -n gem-permessage-deflate-devel
Version:       0.1.4
Release:       alt1
Summary:       Per-message DEFLATE compression extension for WebSocket connections development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета permessage_deflate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(permessage_deflate) = 0.1.4
Requires:      gem(rspec) >= 0 gem(rspec) < 4

%description   -n gem-permessage-deflate-devel
Per-message DEFLATE compression extension for WebSocket connections development
package.

Implements the permessage-deflate WebSocket protocol extension as a plugin for
websocket-extensions.

%description   -n gem-permessage-deflate-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета permessage_deflate.


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

%files         -n gem-permessage-deflate-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-permessage-deflate-devel
%doc README.md


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
- + packaged gem with Ruby Policy 2.0
