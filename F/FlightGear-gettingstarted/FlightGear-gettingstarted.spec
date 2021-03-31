%define origver 2020.3

Name: FlightGear-gettingstarted
Version: %origver
Release: alt1

Summary: open-source flight simulator getting started guide
License: GPLv2+
Group: Documentation

Url: http://www.flightgear.org
# Source-url: https://sourceforge.net/projects/flightgear/files/release-%origver/manual/getstart-en.pdf/download
Source: getstart-en.pdf
BuildArch: noarch
AutoReqProv: no

%description
FlightGear is a free, open-source, multi-platform, and sophisticated
flight simulator framework for the development and pursuit
of interesting flight simulator ideas.

This package contains official Getting Started guile.

You might also enjoy this tutorial:
http://ericbrasseur.org/flight_simulator_tutorial.html

%prep
%setup -c -T

%build

%install
mkdir -p %buildroot
install -pDm644 %SOURCE0 .

%files
%doc getstart-en.pdf

%changelog
* Wed Mar 31 2021 Michael Shigorin <mike@altlinux.org> 2020.3-alt1
- initial package
