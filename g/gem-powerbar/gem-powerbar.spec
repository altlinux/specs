%define        gemname powerbar

Name:          gem-powerbar
Version:       2.0.1
Release:       alt1.1
Summary:       The last progressbar-library you'll ever need
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/busyloop/powerbar
Vcs:           https://github.com/busyloop/powerbar.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hashie) >= 1.1.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hashie) >= 1.1.0
Provides:      gem(powerbar) = 2.0.1


%description
This is PowerBar - The last progressbar-library you'll ever need.

- Detects when stdout is not a terminal and automatically falls back to
logging

* Does not clutter your log-files with ansi-codes! * If your CLI-app can run
interactively and non-interactively (e.g. cronjob) you will automatically get
reasonable progress-output in both modes. * By default prints to stderr but can
call any output-method of your choice (e.g. your favorite Logger).

- Fully customizable; all output is template-driven.

- All output is optional. You may set PowerBar to silently collect progress
information (percentage-done, throughput, ETA, etc.) and then use the computed
values elsewhere in your app.

- All state can be updated at any time. For example: If you're monitoring a
multi-part operation then you can change the status-message of a running
PowerBar to reflect the current state.


%package       -n powerbar-demo
Version:       2.0.1
Release:       alt1.1
Summary:       The last progressbar-library you'll ever need executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета powerbar
Group:         Other
BuildArch:     noarch

Requires:      gem(powerbar) = 2.0.1

%description   -n powerbar-demo
The last progressbar-library you'll ever need executable(s).

This is PowerBar - The last progressbar-library you'll ever need.

- Detects when stdout is not a terminal and automatically falls back to
logging

* Does not clutter your log-files with ansi-codes! * If your CLI-app can run
interactively and non-interactively (e.g. cronjob) you will automatically get
reasonable progress-output in both modes. * By default prints to stderr but can
call any output-method of your choice (e.g. your favorite Logger).

- Fully customizable; all output is template-driven.

- All output is optional. You may set PowerBar to silently collect progress
information (percentage-done, throughput, ETA, etc.) and then use the computed
values elsewhere in your app.

- All state can be updated at any time. For example: If you're monitoring a
multi-part operation then you can change the status-message of a running
PowerBar to reflect the current state.

%description   -n powerbar-demo -l ru_RU.UTF-8
Исполнямка для самоцвета powerbar.


%package       -n gem-powerbar-doc
Version:       2.0.1
Release:       alt1.1
Summary:       The last progressbar-library you'll ever need documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета powerbar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(powerbar) = 2.0.1

%description   -n gem-powerbar-doc
The last progressbar-library you'll ever need documentation files.

This is PowerBar - The last progressbar-library you'll ever need.

- Detects when stdout is not a terminal and automatically falls back to
logging

* Does not clutter your log-files with ansi-codes! * If your CLI-app can run
interactively and non-interactively (e.g. cronjob) you will automatically get
reasonable progress-output in both modes. * By default prints to stderr but can
call any output-method of your choice (e.g. your favorite Logger).

- Fully customizable; all output is template-driven.

- All output is optional. You may set PowerBar to silently collect progress
information (percentage-done, throughput, ETA, etc.) and then use the computed
values elsewhere in your app.

- All state can be updated at any time. For example: If you're monitoring a
multi-part operation then you can change the status-message of a running
PowerBar to reflect the current state.

%description   -n gem-powerbar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета powerbar.


%package       -n gem-powerbar-devel
Version:       2.0.1
Release:       alt1.1
Summary:       The last progressbar-library you'll ever need development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета powerbar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(powerbar) = 2.0.1

%description   -n gem-powerbar-devel
The last progressbar-library you'll ever need development package.

This is PowerBar - The last progressbar-library you'll ever need.

- Detects when stdout is not a terminal and automatically falls back to
logging

* Does not clutter your log-files with ansi-codes! * If your CLI-app can run
interactively and non-interactively (e.g. cronjob) you will automatically get
reasonable progress-output in both modes. * By default prints to stderr but can
call any output-method of your choice (e.g. your favorite Logger).

- Fully customizable; all output is template-driven.

- All output is optional. You may set PowerBar to silently collect progress
information (percentage-done, throughput, ETA, etc.) and then use the computed
values elsewhere in your app.

- All state can be updated at any time. For example: If you're monitoring a
multi-part operation then you can change the status-message of a running
PowerBar to reflect the current state.

%description   -n gem-powerbar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета powerbar.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.MD
%ruby_gemspec
%ruby_gemlibdir

%files         -n powerbar-demo
%doc README.MD
%_bindir/powerbar-demo

%files         -n gem-powerbar-doc
%doc README.MD
%ruby_gemdocdir

%files         -n gem-powerbar-devel
%doc README.MD


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1.1
- ! spec

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
