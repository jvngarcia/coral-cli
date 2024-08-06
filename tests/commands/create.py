from unittest import TestCase, main
import os
from coral_cli.app.commands.create.infrastructure.create_controller import CreateController


class TestCreateController(TestCase):
  def test_create(self):
    controller = CreateController()
    controller.create('test', 'test')
    # Valida que exista el comando test
    self.assertTrue(os.path.exists('commands/cli_test.py'))
    # Crea un rollback, elimina la carpeta y el archivo creado
    os.remove('commands/cli_test.py')
    os.rmdir('commands')

if __name__ == '__main__':
  main()
