%define _unpackaged_files_terminate_build 1
%define pypi_name mido

Name: python3-module-%pypi_name
Version: 1.3.3
Release: alt1

Summary: MIDI Objects for Python
License: MIT
Group: Development/Python3

Url: https://github.com/mido/mido
Vcs: https://github.com/mido/mido
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-pyproject
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)

%add_python3_req_skip mido.backends._common
%add_python3_req_skip rtmidi_python

Requires: python3(rtmidi)

BuildArch: noarch

%description
Mido is a library for working with MIDI messages and ports.

Main Features:
- convenient message objects.
- supports RtMidi, PortMidi and Pygame. New backends are easy to write.
- full support for all 18 messages defined by the MIDI standard.
- standard port API allows all kinds of input and output ports to be used
interchangeably. New port types can be written by subclassing and overriding a
few methods.
- includes a reusable MIDI stream parser.
- full support for MIDI files (read, write, create and play) with complete
access to every message in the file, including all common meta messages.
- can read and write SYX files (binary and plain text).
- implements (somewhat experimental) MIDI over TCP/IP with socket ports. This
allows for example wireless MIDI between two computers.
- includes programs for playing MIDI files, listing ports and serving and
forwarding ports over a network.

%prep
%setup
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/%pypi_name-*
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info
%doc README.rst

%changelog
* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 1.3.3-alt1
- Initial build
