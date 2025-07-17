%define        _unpackaged_files_terminate_build 1
%define        nomen opentelemetry-proto

Name:          %nomen
Version:       0.20.0
Release:       alt1
Group:         Development/Other
Summary:       OpenTelemetry protocol (OTLP) specification and Protobuf definitions
License:       Apache-2.0
Url:           https://opentelemetry-cpp.readthedocs.io/
Vcs:           https://github.com/open-telemetry/opentelemetry-cpp.git

BuildArch:     noarch
Source:        %name-%version.tar

%description
This repository contains the OTLP protocol specification and the corresponding
Language Independent Interface Types (.proto files).

The proto files can be consumed as GIT submodules or copied and built directly
in the consumer project.

The compiled files are published to central repositories (Maven, ...) from
OpenTelemetry client libraries.


%prep
%setup

%install
install -D -m 644 docs/specification.md %buildroot/%_datadir/%nomen/specification.md
cp -rf opentelemetry %buildroot/%_datadir/%nomen/
cp -rf gen/cpp %buildroot/%_datadir/%nomen/
cp -rf gen/ruby %buildroot/%_datadir/%nomen/


%files
%doc README* docs/specification.md
%_datadir/%nomen


%changelog
* Mon Jul 07 2025 Pavel Skrylev <majioa@altlinux.org> 0.20.0-alt1
- Initial build for Sisyphus
