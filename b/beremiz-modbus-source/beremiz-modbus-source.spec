Name: beremiz-modbus-source
Version: 20170318
Release: alt1

Summary: Modbus protocol libraries

License: GPLv3+
Group: Development/Other
Url: https://bitbucket.org/mjsousa/modbus

Packager: Anton Midyukov <antohami@altlinux.org>

Source: mjsousa-modbus-%version.tar

Buildarch: noarch

%description
This directory contains the libararies that implement the modbus protocol
stack.

This protocol has been implemented as a two layer stack. Layer two includes
the mb_master and the mb_slave protocols. Layer one is composed of
the mb_rtu, mb_ascii and mb_tcp protocols.

Layer1 protocols all implement the same interface, defined in mb_layer1.h
Layer2 protocols implement different interfaces, defined in mb_master.h
and mb_slave.h

Which layer1 protocol that will be used by the program will depend on which 
layer1 protocol implementation is linked to the final binary/executable.
It is not possible to define during run-time which layer1 protocol is to
be used. Each compiled program can only support a single layer1 protocol.

Users of these libraries should only use functions defined in the layer2
protocol header files (i.e. mb_master.h and mb_slave.h)

If writing a program that will simultaneously be a master and a slave,
then only use the mb_slave_and_master.h header file!
In this case, do not forget to link the final binary to both the
master and slave protocol implementations (as well as the chosen
layer1 protocol implementation).

%prep
%setup -n mjsousa-modbus-%version

%build

%install
mkdir -p %buildroot%_prefix/src/beremiz-modbus
cp -r * %buildroot%_prefix/src/beremiz-modbus

%files
%doc COPYING COPYING.LESSER README
%_prefix/src/beremiz-modbus

%changelog
* Sun Aug 05 2018 Anton Midyukov <antohami@altlinux.org> 20170318-alt1
- Initial build for ALT Sisyphus
